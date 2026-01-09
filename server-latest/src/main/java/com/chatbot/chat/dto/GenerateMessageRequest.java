package com.chatbot.chat.dto;

import lombok.Data;

@Data
public class GenerateMessageRequest {
    private String content;
    private String image;
}
