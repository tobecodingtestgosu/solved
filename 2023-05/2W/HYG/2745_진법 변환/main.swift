//
//  main.swift
//  2745_진법 변환
//
//  Created by 예강이다 on 2023/05/16.
//

import Foundation

let s = readLine()!.split(separator: " ")
print(Int(s[0],radix: Int(s[1])!)!)

//let input = readLine()!.split(separator: " ")
//let N = input[0]
//let B = Int(input[1])!
//let result = Int(N, radix: B)!
//
//print(result)
