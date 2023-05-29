//
//  main.swift
//  9012_괄호
//
//  Created by 예강이다 on 2023/05/12.
//

import Foundation

let T = Int(readLine()!)!

for _ in 1...T {
    let input = readLine()!
    var cnt = 0
    
    if input[input.startIndex] == ")" {
        print("NO")
        continue
    }
    
//    for char in input {
//        if char == "(" {
//            cnt += 1
//        }
//        else {
//            cnt -= 1
//
//            if cnt < 0 {
//                break
//            }
//        }
//    }
    for char in input {
        (char == "(") ? (cnt += 1) : (cnt -= 1)
        if cnt < 0 { break }
    }
    
    print(cnt == 0 ? "YES" : "NO")
}
