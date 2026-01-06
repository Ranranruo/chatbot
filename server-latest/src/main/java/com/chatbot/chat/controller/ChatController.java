package com.chatbot.chat.controller;

import com.chatbot.auth.security.CustomUserDetails;
import com.chatbot.chat.client.ChatClient;
import com.chatbot.chat.dto.GenerateMessageRequest;
import com.chatbot.chat.dto.GetChatsResponse;
import com.chatbot.chat.dto.MessageDTO;
import com.chatbot.chat.entity.Chat;
import com.chatbot.chat.entity.Message;
import com.chatbot.chat.repository.ChatRepository;
import com.chatbot.chat.repository.MessageRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@RestController
@RequiredArgsConstructor
@RequestMapping("/chats")
public class ChatController {
    private final ChatRepository chatRepository;
    private final MessageRepository messageRepository;
    private final ChatClient chatClient;

    /**
     * 로그인한 사용자의 채팅 목록 조회
     * @return {@link GetChatsResponse}
     */
    @GetMapping
    public GetChatsResponse getChats(@AuthenticationPrincipal CustomUserDetails customUserDetails) {
        GetChatsResponse response = new GetChatsResponse();
        response.setChats(chatRepository.findAllByMemberId(customUserDetails.getId()));
        return response;
    }

    /**
     * 로그인한 사용자 새 채팅 생성
     * @return true
     */
    @PostMapping
    public boolean createChat(
            @AuthenticationPrincipal CustomUserDetails customUserDetails
    ) {
        Chat chat = new Chat();
        chat.setMemberId(customUserDetails.getId());
        chat.setTitle("새 채팅");
        chatRepository.save(chat);
        return true;
    }

    /**
     * chat_id를 path로 받아 채팅 메세지 목록 조회
     * @return List<{@link Message}>
     */
    @GetMapping("/{chat_id}/message")
    public List<Message> getMessages(
            @PathVariable("chat_id") Long chatId,
            @AuthenticationPrincipal CustomUserDetails customUserDetails
    ) {
        return messageRepository.findAllByChatId(chatId);
    }

    /**
     * chat_id를 path로 받아 프롬포트 메세지를 받아 새 메세지 생성
     * @return true
     */
    @PostMapping("/{chat_id}/message")
    public boolean generateMessage(
            @PathVariable("chat_id") Long chatId,
            @AuthenticationPrincipal CustomUserDetails customUserDetails,
            @RequestBody GenerateMessageRequest request
    ) {
        Message message = new Message();
        message.setChatId(chatId);
        message.setContent(request.getContent());
        message.setImage(request.getImage());
        message.setRole("user");
        messageRepository.save(message);
        List<Message> messages = messageRepository.findAllByChatId(chatId);
        List<MessageDTO> clientMessages = messages.stream().map(data -> {
            MessageDTO dto = new MessageDTO();
            dto.setRole(data.getRole());
            dto.setContent(data.getContent());
            if(data.getImage()!=null)
                dto.setImages(List.of(data.getImage()));
            else
                dto.setImages(List.of(""));
            return dto;
        }).collect(Collectors.toList());
        MessageDTO result = chatClient.generateMessage(clientMessages);
        Message responseMessage = new Message();
        responseMessage.setChatId(chatId);
        responseMessage.setContent(result.getContent());
        responseMessage.setRole(result.getRole());
        messageRepository.save(responseMessage);
        return true;
    }
}
