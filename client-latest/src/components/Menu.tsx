interface MenuProps {
    children: string | React.ReactNode
    onClick?: ()=> void
}

const Menu = ({
    children,
    onClick
}:MenuProps ) => {
    return (
        <button
            className="mb-1 m-2 p-2.5 pl-4 text-left cursor-pointer bg-gray-800 rounded-xl hover:bg-gray-700"
            onClick={onClick}
        >
            {children}
        </button>
    );
}
export default Menu;