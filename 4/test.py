
# 재질별 밀도 (g/cm3)
DENSITY = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85
}

# 화성 중력 계수 (화성 중력 / 지구 중력)
MARS_GRAVITY_FACTOR =3.73 / 9.807

# 전역 변수 선언
global_material = ''
global_diameter = 0
global_thickness = 0
global_area = 0
global_weight = 0

def sphere_area(diameter, material='유리', thickness=1):
    '''
    지름 (m), 재질, 두께 (cm)를 입력 받아 반구체 돔의 전체 면적과 화성에서의 무게를 계산하는 함수.
    계산식:
      - 반구체의 곡면적 = 2 * π * r^2 (r: cm 단위)
      - 재료의 부피 = 면적 * 두께 (cm3)
      - 질량 = 밀도 * 부피 (g)
      - 질량(kg) = 질량 / 1000
      - 화성에서의 무게(kg) = 질량(kg) * (화성중력/지구중력)
    '''
    # 단위 변환: m -> cm
    diameter_cm = diameter * 100
    radius_cm = diameter_cm / 2
    
    # 반구체의 곡면적 (cm^2)
    area = 2 * 3.14 * (radius_cm ** 2)
    
    # 재료의 부피 (cm^3) = 면적 * 두께
    volume = area * thickness
    
    # 입력된 재질의 밀도 확인, 없으면 기본 '유리' 사용
    density = DENSITY.get(material, DENSITY['유리'])
    
    # 질량 (g)
    mass_g = density * volume
    # 질량 (kg)
    mass_kg = mass_g / 1000
    # 화성에서의 무게 (kg)
    weight = mass_kg * MARS_GRAVITY_FACTOR
    
    # 소수점 3자리까지 반올림
    area = round(area, 3)
    weight = round(weight, 3)
    
    return area, weight

def main():
    global global_material, global_diameter, global_thickness, global_area, global_weight
    while True:
        try:
            # 사용자로부터 입력 받기
            diameter_input = input('지름(미터 단위, 0 입력 시 종료): ')
            diameter = float(diameter_input)
            if diameter == 0:
                break
            if diameter < 0:
                print('지름은 0보다 커야 합니다.')
                continue
        except ValueError:
            print('지름은 숫자로 입력해 주세요.')
            continue

        material_input = input('재질(유리/알루미늄/탄소강, 기본값: 유리): ')
        # 입력이 없으면 기본값 사용
        if material_input.strip() == '':
            material = '유리'
        else:
            material = material_input.strip()
            if material not in DENSITY:
                print('입력한 재질이 존재하지 않습니다. 기본값(유리)를 사용합니다.')
                material = '유리'
        
        try:
            thickness_input = input('두께(cm 단위, 기본값: 1): ')
            if thickness_input.strip() == '':
                thickness = 1
            else:
                thickness = float(thickness_input)
                if thickness <= 0:
                    print('두께는 0보다 커야 합니다. 기본값(1cm)을 사용합니다.')
                    thickness = 1
        except ValueError:
            print('두께는 숫자로 입력해 주세요. 기본값(1cm)을 사용합니다.')
            thickness = 1
        
        # 계산 수행
        area, weight = sphere_area(diameter, material, thickness)
        
        # 전역 변수에 결과 저장
        global_material = material
        global_diameter = diameter
        global_thickness = thickness
        global_area = area
        global_weight = weight
        
        # 결과 출력 (소수점 이하 3자리까지 출력)
        print('\n재질 =⇒ {0}, 지름 =⇒ {1:.3f}, 두께 =⇒ {2:.3f}, 면적 =⇒ {3:.3f}, 무게 =⇒ {4:.3f} kg'.format(
            global_material, global_diameter, global_thickness, global_area, global_weight))
        print()

if __name__ == '__main__':
    main()
