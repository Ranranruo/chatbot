import { useState } from "react";
import { useNavigate } from "react-router-dom";
import useAuthApi from "../api/useAuthApi";

const SignInPage = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const authApi = useAuthApi();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("username", username);
    formData.append("password", password);
    const isLoggedIn = await authApi.signIn(formData);
    if(isLoggedIn){
        alert("로그인 성공")
        navigate("/")
    } else {
        alert("로그인 실패")
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-gray-900 text-gray-100">
      <form
        className="bg-gray-800 p-8 rounded-xl w-96 shadow-lg flex flex-col space-y-6"
        onSubmit={handleSubmit}
      >
        <h1 className="text-2xl font-bold text-center">로그인</h1>

        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="p-3 rounded-lg border border-gray-600 bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="p-3 rounded-lg border border-gray-600 bg-gray-700 text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />

        <button
          type="submit"
          className="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-lg font-semibold"
        >
          로그인
        </button>

        <p className="text-gray-400 text-center text-sm">
          계정이 없으신가요? <span className="text-blue-500 cursor-pointer" onClick={()=> navigate("/sign-up")}>회원가입</span>
        </p>
      </form>
    </div>
  );
};

export default SignInPage;
