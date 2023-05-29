//
//  main.swift
//  10828_스택
//
//  Created by 예강이다 on 2023/05/11.
//

import Foundation

let N = Int(readLine()!)!
var stack = [Int]()

for _ in 1...N {
    let command = readLine()!.split(separator: " ").map{ String($0) }
    
    if command[0] == "push" {
        stack.append(Int(command[1])!)
    }
    
    else if command[0] == "pop" {
        print(!stack.isEmpty ? stack.remove(at: stack.count - 1) : -1)
    }
    
    else if command[0] == "size" {
        print(stack.count)
    }
    
    else if command[0] == "empty" {
        print(stack.isEmpty ? 1 : 0)
    }
    
    else if command[0] == "top" {
        print(!stack.isEmpty ? stack[stack.count - 1] : -1)
    }
}
