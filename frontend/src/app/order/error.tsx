"use client";
import { useEffect } from "react";
import { ErrorProps } from "app/app/types";

export default function Error({ error, reset }: ErrorProps) {
  useEffect(() => {
    console.log("Tracking event error: ", error);
  }, [error]);
  return (
    <div>
      <h1>:C</h1>
      <p>Ha ocurrido un error.</p>
      <button onClick={reset}> Intentar de nuevo</button>
    </div>
  );
}
