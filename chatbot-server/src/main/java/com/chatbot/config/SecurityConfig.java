package com.chatbot.config;

import com.chatbot.config.handler.LoginFailureHandler;
import com.chatbot.config.handler.UnauthorizedEntryPoint;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.provisioning.InMemoryUserDetailsManager;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.web.cors.CorsConfigurationSource;

@EnableWebSecurity
@Configuration
@RequiredArgsConstructor
public class SecurityConfig {
    private final UnauthorizedEntryPoint unauthorizedEntryPoint;
    private final CorsConfigurationSource corsConfigurationSource;
    private final LoginFailureHandler loginFailureHandler;
    private final UserDetailsService userDetailsService;
    @Bean
    public BCryptPasswordEncoder bCryptPasswordEncoder() {
        return new BCryptPasswordEncoder();
    }


    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http, UnauthorizedEntryPoint unauthorizedEntryPoint) throws Exception {
        return http
                .authorizeHttpRequests((auth) -> auth
                        .requestMatchers("/sign-in").permitAll()
                        .anyRequest().authenticated()
                )
                .csrf((csrf)->csrf.disable())
                .userDetailsService(userDetailsService)
                .formLogin(form -> form
                        .loginProcessingUrl("/sign-in")
                        .usernameParameter("username")
                        .passwordParameter("password")
                        .failureHandler(loginFailureHandler)
                        .successHandler((request, response, authentication) -> {})
                )
                .cors(cors -> cors.configurationSource(corsConfigurationSource))
                .exceptionHandling(handling -> handling
                        .authenticationEntryPoint(unauthorizedEntryPoint)
                )
                .logout(logout -> logout
                        .logoutUrl("/logout")
                )
                .build();
    }
}
