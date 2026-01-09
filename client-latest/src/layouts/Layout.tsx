import { useEffect, useState } from "react";
import Menu from "../components/Menu";
import { Outlet, useNavigate } from "react-router-dom";
import useAuthApi from "../api/useAuthApi";
import useChatApi from "../api/useChatApi";
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL
console.log(API_BASE_URL)
interface chats {
    id: number,
    memberId: number,
    title: string
}
const Layout = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState("username");
    const [render, setRender] = useState(true);
    const [chats, setChats] = useState<chats[]>([]);
    const authApi = useAuthApi();
    const chatApi = useChatApi();
    // 로그인 확인
    authApi.isAuthenticated().then(isAuthenticated=>{
        if(!isAuthenticated)
            // 로그인 상태가 아니면 로그인 페이지로 이동
            navigate("/sign-in")
    });
    useEffect(()=>{
        // 이름 표시
        authApi.getUsername().then(username=>setUsername(username))
        // 채팅 목록 표시
        chatApi.getChats().then(data=>setChats(()=>data.chats));
    },[render]);

    const newChat = async () => {
        // 새 채팅 생성 후 렌더링
        chatApi.createChat().then(()=>setRender(prev=>!prev))
    }
    return (
        <div className="flex h-screen bg-gray-900 text-gray-100">
            <aside className="w-64 bg-gray-800 border-r border-gray-700 flex flex-col">
                <div className="flex-1 flex flex-col overflow-y-scroll">
                    <Menu onClick={newChat}>새 채팅 만들기</Menu>
                    {chats.map(chat => (
                    <Menu
                        onClick={()=>{navigate(`/chat/${chat.id}`); setRender(prev=>!prev)}}
                    >
                        {chat.title}
                    </Menu>))}
                </div>
                <div className="mt-auto flex flex-col">
                    <Menu>
                        {username} (로그아웃)
                    </Menu>
                </div>
            </aside>
            <section className="flex-1 flex flex-col p-4 overflow-y-auto space-y-4">
                <Outlet />
            </section>
        </div>
    );
}
export default Layout;