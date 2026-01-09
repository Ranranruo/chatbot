const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const useMessageApi = () => {
    const getMessages = async (chatId: number) => {
        return await fetch(`${API_BASE_URL}/chats/${chatId}/message`, {
            credentials: 'include'
        }).then(response=>response.json())
    }
    const generateMessage = async (chatId: number, content: string, image: string) => {
        const response = await fetch(`${API_BASE_URL}/chats/${chatId}/message`, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': "application/json"
            },
            body: JSON.stringify({
                content,
                image
            })
        })
        if(response.status === 200) return true;
        return false;
    }
    return { getMessages, generateMessage }
}

export default useMessageApi;