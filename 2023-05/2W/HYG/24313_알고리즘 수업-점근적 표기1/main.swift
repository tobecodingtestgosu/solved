//
//  main.swift
//  24313_알고리즘 수업-점근적 표기1
//
//  Created by 예강이다 on 2023/05/16.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let a1 = input[0]
let a0 = input[1]

let c = Int(readLine()!)!
let n = Int(readLine()!)!

if (a1 * n + a0) <= (c * n) && (c >= a1) {
    print(1)
} else {
    print(0)
}
