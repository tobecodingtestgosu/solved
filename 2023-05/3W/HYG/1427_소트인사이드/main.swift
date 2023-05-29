//
//  main.swift
//  1427_소트인사이드
//
//  Created by 예강이다 on 2023/05/21.
//

import Foundation

var input = String(Int(readLine()!)!).sorted(by: >)
for i in 0..<input.count {
    print("\(input[i])", terminator: "")
}
