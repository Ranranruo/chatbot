"use client"
import Button from "@/components/Button";
import { IoSearch } from "react-icons/io5";
import { FaArrowRight } from "react-icons/fa";
import { useEffect } from "react";
import { useThemeStore } from "@/stores/useThemeStore";
const Home = () => {
  return ( 
    <>
      <Button.Primary 
        leftIcon={<IoSearch/>}
        rightIcon={<FaArrowRight/>}
      >
        Default
      </Button.Primary>
    </>
  );
}
export default Home;