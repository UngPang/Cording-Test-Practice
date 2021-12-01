def solution(phone_book):
    phone_book = sorted(phone_book) # 문자열 정렬
    
    phone_nums = set(phone_book) # phone_book은 중복되는 항목이 없음
    
    for i in range(0, len(phone_book)):
        phone = phone_book[i] # 전화번호 하나를 선택한다.
        
        # 해당 전화번호를 1부터 길이 만큼 잘라가며 같은 요소가 있는지 체크한다.
        for j in range(1, len(phone)):
            if phone[:j] in phone_nums:
                return False # 같은 요소가 있으면 false 반환
    
    return True
