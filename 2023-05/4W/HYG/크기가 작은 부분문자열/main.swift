//
//  main.swift
//  크기가 작은 부분문자열
//
//  Created by 예강이다 on 2023/05/26.
//

import Foundation

let t = "3141592"
let p = "271"

var result = 0
let tLength = t.count
let pLength = p.count

for i in 0..<tLength - pLength + 1 {
    let startIdx = t.index(t.startIndex, offsetBy: i)
    let endIdx = t.index(t.startIndex, offsetBy: i + pLength - 1)
    let range = startIdx...endIdx
    
    if Int64(t[range])! <= Int64(p)! {
        result += 1
    }
}



//7 3 = 5
//12 1 = 12
//5 2 = 4
