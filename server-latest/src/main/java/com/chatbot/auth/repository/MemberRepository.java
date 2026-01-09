package com.chatbot.auth.repository;

import com.chatbot.auth.entity.Member;
import jakarta.servlet.http.HttpSession;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MemberRepository extends JpaRepository<Member,Integer> {
    Member findByUsername(String username);
}
