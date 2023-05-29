//
//  main.swift
//  1874_스택 수열
//
//  Created by 예강이다 on 2023/05/12.
//

import Foundation

let n = Int(readLine()!)!

var stack = [Int]()
var numList = [Int]()
var result = [String]()
var cnt = 1

for _ in 1...n {
    let num = Int(readLine()!)!
    numList.append(num)
}
numList.reverse()

for i in 1...n {
    let top = stack.last
    
    if top != numList.last! {
        result.append("+")
        stack.append(i)
        
        while !stack.isEmpty {
            let top = stack.last
            if top == numList.last! {
                result.append("-")
                stack.removeLast()
                numList.removeLast()
                
            } else {
                break
            }
        }
    } else {
        result.append("-")
        stack.removeLast()
    }
}

if numList.isEmpty {
    for i in result {
        print("\(i)")
    }
} else {
    print("NO")
}

