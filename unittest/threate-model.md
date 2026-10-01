# Threat Model - json_search() (Nhom08)

## 1. Bối cảnh
json_search(key, input_object, role) tìm đệ quy một key trong JSON trả về từ
API giám sát hạ tầng mạng (DNAC) và trả về danh sách các cặp key/value.

## 2. Actor / Role
| Role | Mục đích gọi hàm |
|------|------------------|
| admin | Quản trị, cấu hình thiết bị, cần mọi trường kể cả apiKey |
| operator | Vận hành, xử lý sự cố, cần IP quản trị và tóm tắt sự cố |
| viewer | Chỉ xem tình trạng chung, chỉ cần tóm tắt sự cố |
| Không có role / role lạ | Không được coi là actor hợp lệ |

## 3. Asset nhạy cảm
| Asset (key) | Ví dụ giá trị | Mức độ | Vì sao nhạy cảm |
|-------------|---------------|--------|-----------------|
| apiKey | SNMP-COMMUNITY-STRING-... | Cao | Chuỗi xác thực SNMP, kẻ tấn công dùng để truy vấn/cấu hình thiết bị |
| managementIpAddress | 10.10.20.21 | Trung bình | Lộ địa chỉ quản trị, hỗ trợ trinh sát và tấn công trực tiếp thiết bị |
| issueSummary | Network Device ... Unreachable | Thấp | Thông tin sự cố chung |

## 4. Trust boundary
- Ranh giới giữa dữ liệu thô từ API giám sát (chứa mọi trường) và người gọi
TODO: chép tiếp phần còn lại của mục 4 và các mục sau (threat T1-T4) từ file gốc
EOF
