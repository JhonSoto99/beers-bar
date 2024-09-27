import Link from "next/link";

export default function Home() {
  return (
    <main>
        <Link href="/order">
            <h1>Ir a ver la orden</h1>
        </Link>
    </main>
  );
}
