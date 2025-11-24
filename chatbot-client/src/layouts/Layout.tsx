import { useEffect, useState } from "react";
import Menu from "../components/Menu";
import { Outlet, useNavigate } from "react-router-dom";

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
    useEffect(()=>{
        fetch("http://localhost:8080/auth/username", {
            credentials: 'include'
        }).then(data=>data.text()).then(data=>setUsername(data));
        fetch("http://localhost:8080/chats", {
            credentials: 'include'
        }).then(data=>data.json()).then(data=>setChats(()=>data.chats));
    },[render]);
    useEffect(()=>{
        console.log(chats)
    }, [chats]);

    const newChat = async () => {
        fetch("http://localhost:8080/chats", {
            method: "POST",
            credentials: 'include'
        }).then(()=>setRender((prev) => !prev))
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