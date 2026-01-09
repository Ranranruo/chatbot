package com.chatbot.chat.client;

import com.chatbot.chat.dto.MessageDTO;
import com.chatbot.chat.entity.Message;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.List;
import java.util.Map;


@FeignClient(
    name = "chatClient",
    url = "${ai.server.base-url}"
)
public interface ChatClient {
    @PostMapping("/chat")
    MessageDTO generateMessage(@RequestBody List<MessageDTO> request);

}
