# Security Requirements - json_search() (Nhom08)

Các requirement suy ra từ threat model (threate-model.md).

| ID | Requirement | Threat | Kiểm chứng bằng test |
|----|-------------|--------|----------------------|
| SR1 | Hệ thống chỉ trả về giá trị của trường apiKey cho role admin. Role operator và viewer nhận danh sách rỗng. | T1, T2 | test_viewer_cannot_read_apikey, test_operator_cannot_read_apikey |
| SR2 | Hệ thống chỉ trả về giá trị của trường managementIpAddress cho role admin và operator. Role viewer nhận danh sách rỗng. | T1 | test_viewer_cannot_read_management_ip |
| SR3 | Role là None, rỗng, hoặc không nằm trong POLICY (ví dụ "root") không được đọc bất kỳ trường nào được bảo vệ (deny by default). | T3 | test_no_role_cannot_read_protected, test_unknown_role_denied |
| SR4 | Việc kiểm tra role phải áp dụng cho mọi kết quả tìm thấy ở mọi độ sâu lồng nhau, không chỉ cấp ngoài cùng. | T4 | test_wrong_role_cannot_read_secret (apiKey nằm sâu 4 cấp) |
| SR5 | Trường issueSummary được phép đọc bởi cả admin, operator và viewer. | (chức năng) | test_issue_summary_allowed_for_all_roles |
| SR6 | Hàm không được ghi log hoặc in giá trị của trường bị từ chối. | T1 | rà soát code |
EOF