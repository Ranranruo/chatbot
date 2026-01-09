import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import useMessageApi from "../api/useMessageApi";

interface Chat {
    role: string,
    content: string,
    image: string
}

const ChatPage = () => {
    const location = useLocation();
    const chatId = location.pathname.split("/")[2];
    const [input, setInput] = useState("");
    const [image, setImage] = useState("");
    const [chats, setChats] = useState<Chat[]>([]);
    const [render, setRender] = useState(true);

    const messageApi = useMessageApi();

    useEffect(() => {
        messageApi.getMessages(parseInt(chatId))
            .then(data => setChats(() => data))
    }, [render, chatId])
    const handleSubmit = async () => {
        setChats(prev=>[...prev, {role: "user",content: input,image: image}])
        
        const isGenerated = await messageApi.generateMessage(parseInt(chatId), input, image);
        if(isGenerated) {
            setRender(prev => !prev)
            setInput(()=>"")   
            setImage(()=>"")
        }
    }
    return (
        <div className="flex-1 flex flex-col bg-gray-900 rounded-lg shadow-inner">
            <div className="flex-1 p-4 overflow-y-auto space-y-4 scrollbar-thin scrollbar-thumb-gray-600 scrollbar-track-gray-800">
                {chats.map((chat, idx) => (
                    <div
                        key={idx}
                        className={`flex ${chat.role === "user" ? "justify-end" : "justify-start"}`}
                    >
                        <div
                            className={`p-3 rounded-xl max-w-xs break-words ${chat.role === "user"
                                    ? "bg-blue-600 text-white"
                                    : "bg-gray-700 text-gray-100"
                                }`}
                        >
                            <p>{chat.content}</p>
                            {chat.image && (
                                <img
                                    src={`data:image/png;base64,${chat.image}`}
                                    alt="uploaded"
                                    className="mt-2 rounded-lg"
                                />
                            )}
                        </div>
                    </div>
                ))}
            </div>

            <div className="flex flex-col p-4 border-t border-gray-700 bg-gray-800 space-y-2">
            <div className="flex items-center">
                    <input type="file" accept="image/*" hidden id="img"
                        onChange={(e) => {
                            const reader = new FileReader();
                            reader.onload = () => {
                                if (typeof reader.result == "string") {
                                    const base64 = reader.result.split(",")[1];
                                    setImage(() => base64);
                                    e.target.value = ""
                                    e.target.files = null
                                }
                            }
                            if (e.target.files != null)
                                reader.readAsDataURL(e.target.files[0]);
                        }}
                    />
                    <label htmlFor="img" className="p-2 hover:bg-gray-700 rounded-lg">
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            className="h-6 w-6 text-gray-100"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="currentColor"
                        >
                            <path
                                strokeLinecap="round"
                                strokeLinejoin="round"
                                strokeWidth={2}
                                d="M15.172 7l-6.586 6.586a2 2 0 102.828 2.828L18 9.828m-2.828-2.828L21 4"
                            />
                        </svg>
                    </label>

                    <input
                        type="text"
                        placeholder="메시지 입력..."
                        className="flex-1 p-3 ml-2 rounded-l-xl border border-gray-600 bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
                        onChange={(e) => setInput(e.target.value)}
                        value={input}
                    />
                    <button
                        className="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-r-xl ml-1"
                        onClick={handleSubmit}
                    >
                        전송
                    </button>
                </div>
                <p className="text-sm text-gray-400">선택된 파일: {image ? "있음" : "없음"}</p>
            </div>
        </div>

    );
};

export default ChatPage;
