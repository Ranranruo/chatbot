package com.chatbot.chat.repository;

import com.chatbot.chat.entity.Chat;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface ChatRepository extends JpaRepository<Chat, Long> {
    List<Chat> findAllByMemberId(Long memberId);
}
