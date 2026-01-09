const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const useChatApi = () => {
    /**
     * 채팅 목록을 가져오는 함수
     */
    const getChats = async () => {
        return await fetch(`${API_BASE_URL}/chats`, {
            credentials: 'include'
        }).then(data=>data.json());
    }
    /**
     * 새 채팅을 생성하는 함수
     */
    const createChat = async () => {
        await fetch(`${API_BASE_URL}/chats`, {
            method: 'POST',
            credentials: 'include'
        })
    }
    return { getChats, createChat }
}
export default useChatApi