import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./layouts/Layout";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import SignInPage from "./pages/SignInPage";
import ChatPage from "./pages/ChatPage";
const queryClient = new QueryClient();
function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route path="/chat/:id" element={<ChatPage />}/>
          </Route>
          <Route path="/sign-in" element={<SignInPage/>} />
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  )
}

export default App
