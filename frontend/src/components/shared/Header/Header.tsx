import Link from "next/link";

export const Header = () => {
  return (
    <header className="bg-gray-800 shadow">
      <nav className="flex justify-center p-4">
        <ul className="flex space-x-4">
          <li>
            <Link href="/" className="text-white hover:text-red-500">
              Home
            </Link>
          </li>
          <li>
            <Link href="/order" className="text-white hover:text-red-500">
              Order
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};
