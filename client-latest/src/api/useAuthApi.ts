const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

const useAuthApi = () => {
    const signIn = async (formData: FormData) => {
        const response = await fetch(`${API_BASE_URL}/sign-in`, {
            method: 'POST',
            body: formData,
            credentials: 'include'
        })
        if(response.status === 200) return true;
        return false;
    }
    const isAuthenticated = async () => {
        const response = await fetch(`${API_BASE_URL}/auth/me`, {
            credentials: "include"
        });
        if(response.status === 401) return false;
        return true;
    }
    const getUsername = async () => {
        return await fetch(`${API_BASE_URL}/auth/username`, {
            credentials: 'include'
        }).then(data=>data.text());
    }
    return { signIn, isAuthenticated, getUsername }
}

export default useAuthApi;