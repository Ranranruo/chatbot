package com.chatbot.auth.controller;

import com.chatbot.auth.repository.MemberRepository;
import com.chatbot.auth.security.CustomUserDetails;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/auth")
public class AuthController {
    private final MemberRepository memberRepository;
    @GetMapping("/")
    public String test(HttpSession httpSession) {
        System.out.println(httpSession.getId());
        return "Hello World!";
    }
    @GetMapping("/username")
    public String getUsername(@AuthenticationPrincipal CustomUserDetails customUserDetails) {
        return customUserDetails.getUsername();
    }
}
