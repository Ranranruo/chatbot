"use client"
import { useThemeStore } from "@/stores/useThemeStore";

interface ButtonProps {
    children?: string;
    type: 'text' | 'icon' | 'number',
    size: 'default' | 'small'
    leftIcon?: React.ReactNode;
    rightIcon?: React.ReactNode;
}
const BASE = {
    common: "rounded-lg px-4 flex justify-center items-center",
    default: "py-3 gap-2 text-sm",
    small: "py-2 gap-1 text-xs"
};


const Primary = ({
    children,
    type='text',
    size='default',
    leftIcon,
    rightIcon
}: ButtonProps) => {
    const isDark = useThemeStore((state) => state.isDark);
    return (
        <button
            className={`
                ${BASE.common}
                ${BASE[size]}
                gap-1
                text-neutral-100
                bg-linear-to-t from-blue-600 to-blue-500
                border border-blue-800
                shadow-[0_4px_6px_-1px_rgba(59,130,246,0.17),0_2px_4px_-2px_rgba(59,130,246,0.17),inset_0_2px_1px_0_rgba(255,255,255,0.22),inset_0_-2px_0.3px_0_rgba(14,56,125,0.18)]
                `
            }>
            {leftIcon}
            <p className="font-medium">
                {children}
            </p>
            {rightIcon}
        </button>
// shadow-md shadow-blue-500/17,_inset_0_2px_1px_0_rgba(255,255,255,0.22)]
    );
}
const Button = { Primary }
export default Button;