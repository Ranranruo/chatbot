package com.chatbot.auth.controller;

import com.chatbot.auth.dto.GetMemberResponse;
import com.chatbot.auth.repository.MemberRepository;
import com.chatbot.auth.security.CustomUserDetails;
import feign.FeignException;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.HttpClientErrorException;

@RestController
@RequiredArgsConstructor
@RequestMapping("/auth")
public class AuthController {
    private final MemberRepository memberRepository;
    @GetMapping("/me")
    public GetMemberResponse getMember (
            @AuthenticationPrincipal CustomUserDetails userDetails
    ) {
        if(userDetails == null) ResponseEntity.status(HttpStatus.UNAUTHORIZED);
        GetMemberResponse response = new GetMemberResponse();
        response.setId(userDetails.getId());
        response.setUsername(userDetails.getUsername());
        return response;
    }
    @GetMapping("/username")
    public String getUsername(
            @AuthenticationPrincipal CustomUserDetails userDetails
    ) {
        return userDetails.getUsername();
    }
}
