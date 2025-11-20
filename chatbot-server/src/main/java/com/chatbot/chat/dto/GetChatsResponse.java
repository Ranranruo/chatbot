package com.chatbot.chat.dto;

import com.chatbot.chat.entity.Chat;
import lombok.Data;

import java.util.List;

@Data
public class GetChatsResponse {
    private List<Chat> chats;
}
