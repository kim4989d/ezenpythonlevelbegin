class raise_4:

    def raise4(self):
        try:
            value = int(input('값을 입력:'))

            if(value>5):
                raise
        except:
            raise Exception('에러 발생 ')
            print('에러 발생 ')

        finally:
            print('에러가 나든 않나든 무저건 실행 ')



ra=raise_4()
ra.raise4()