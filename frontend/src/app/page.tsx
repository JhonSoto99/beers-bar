import Link from "next/link";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center h-screen text-center">
      <h1 className="text-3xl font-bold mb-4">¡Welcome!</h1>
      <Link href="/order" className="text-blue-500 hover:underline">
        Go to view your order
      </Link>
    </main>
  );
}
