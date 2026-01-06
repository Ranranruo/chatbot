package com.chatbot.chat.repository;

import com.chatbot.chat.entity.Message;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface MessageRepository extends JpaRepository<Message, String> {
    List<Message> findAllByChatId(Long chatId);
}
