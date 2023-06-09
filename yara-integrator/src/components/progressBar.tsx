import React from "react";

export interface ProgressBarProps {
  progress: number;
  className?: string;
  variant?: "primary" | "secondary"
}

export const ProgressBar = ({ progress, className }: ProgressBarProps) => {
  const colors = {
    "primary": "bg-white"
  }
  return (
    <div className={`h-7 w-full bg-white ${className ?? ""}`}>
      <div
        className="h-7 bg-primary"
        style={{ width: `${progress}%`, transition: "0.2s" }}
      ></div>
    </div>
  );
};
