import numpy as np

def main():
    arr1 = np.genfromtxt('mars_base_main_parts-001.csv', delimiter=',', skip_header=1, encoding='utf-8-sig', dtype=float)
    arr2 = np.genfromtxt('mars_base_main_parts-002.csv', delimiter=',', skip_header=1, encoding='utf-8-sig', dtype=float)
    arr3 = np.genfromtxt('mars_base_main_parts-003.csv', delimiter=',', skip_header=1, encoding='utf-8-sig', dtype=float)
    # 배열 병합
    parts = np.concatenate((arr1, arr2, arr3), axis=0)
    # 모든 행에서 NaN만 포함하는 열을 제거 (비숫자 열 제거)
    valid_cols = ~np.all(np.isnan(parts), axis=0)
    parts = parts[:, valid_cols]
    # 남은 데이터에서 NaN을 무시하고 각 부품의 평균 계산
    means = np.nanmean(parts, axis=1)
    # 평균이 50보다 작은 부품 선택
    weak_mask = means < 50
    parts_to_work_on = parts[weak_mask]
    # 예외 처리와 함께 약한 부품을 CSV로 저장
    try:
        np.savetxt('parts_to_work_on.csv', parts_to_work_on, delimiter=',', fmt='%f')
    except IOError as err:
        print(f'parts_to_work_on.csv 저장 중 오류: {err}')
    # 보너스: 저장된 파일 다시 읽어 전치 계산
    try:
        parts2 = np.loadtxt('parts_to_work_on.csv', delimiter=',')
        parts3 = parts2.T
        print(parts3)
    except IOError as err:
        print(f'parts_to_work_on.csv 읽는 중 오류: {err}')


if __name__ == '__main__':
    main()
