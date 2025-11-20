package com.chatbot;

import com.chatbot.auth.entity.Member;
import com.chatbot.auth.repository.MemberRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@SpringBootTest
class ChatbotApplicationTests {
    @Autowired
    private MemberRepository memberRepository;
    @Autowired
    private BCryptPasswordEncoder bCryptPasswordEncoder;
	@Test
	void contextLoads() {
        Member  member = new Member();
        member.setUsername("admin");
        member.setPassword(bCryptPasswordEncoder.encode("1234"));
        memberRepository.save(member);
	}

}
