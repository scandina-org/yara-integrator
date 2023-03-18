import { useRouter } from "next/router";
import React, { useState } from "react";
import { Button } from "./button";

export interface Rule {
  name: string;
  path: string;
}
interface RuleRowProps extends Rule {
  onSelectRow: () => void;
}
const Tickbox = ({
  isTicked,
  onTicked,
}: {
  isTicked: boolean;
  onTicked: () => void;
}) => {
  return (
    <div
      onClick={onTicked}
      className="h-4 w-4 border-2 border-slate-400 rounded-sm"
      style={{
        backgroundColor: isTicked ? "#8ad645" : "transparent",
        transition: "background-color 0.2s",
      }}
    ></div>
  );
};
export const RuleRow = ({ name, path, onSelectRow }: RuleRowProps) => {
  const router = useRouter();
  const [isSelected, setSelected] = useState(false);
  const onClick = () => {
    onSelectRow();
    setSelected((prev) => !prev);
  };
  return (
    <>
      <div className="p-2 col-span-2 bg-white text-black border-b flex flex-row items-center">
        <Tickbox isTicked={isSelected} onTicked={onClick}></Tickbox>
        <div className="ml-2">{name}</div>
      </div>
      <div className="p-2 bg-white col-span-1 flex flex-row justify-end border-b">
        <div className="w-full max-w-[5rem]">
          <Button onClick={() => router.push(`/rules/edit/${name}`)}>
            Edit
          </Button>
        </div>
      </div>
    </>
  );
};
