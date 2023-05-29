//
//  main.swift
//  11005_진법 변환2
//
//  Created by 예강이다 on 2023/05/16.
//

import Foundation

let n = readLine()!.split(separator: " ").map{ Int($0)! }
print(String(n[0], radix: n[1]).uppercased())

//let input = readLine()!.split(separator: " ")
//
//let N = input[0]
//let B = input[1]
//
//let result = String(Int(N)!, radix: Int(B)!)
//
//print(result.uppercased())
