package com.chatbot.chat.dto;

import lombok.Data;

import java.util.List;

@Data
public class MessageDTO {
    String role;
    String content;
    List<String> images;
}
