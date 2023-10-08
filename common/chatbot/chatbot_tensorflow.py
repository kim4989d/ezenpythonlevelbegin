import tensorflow as tf
import numpy as np

# 데이터 준비
input_texts = ['안녕?', '안녕하세요.', '좋은 아침이에요!', '넌 어떻게 지내니?', '날씨 어때?', '뭐해?']
target_texts = ['안녕!', '안녕하세요!', '좋은 아침이에요!', '난 잘 지내고 있어, 고마워!', '날씨는 맑아요.', '너랑 대화하고 있어요.']

# 토큰화 및 단어 집합 생성
tokenizer = tf.keras.layers.TextVectorization(output_mode='int')
tokenizer.adapt(input_texts + target_texts)
vocab_size = len(tokenizer.get_vocabulary())

# 데이터를 숫자로 변환
input_sequences = tokenizer(input_texts)
target_sequences = tokenizer(target_texts)

# 모델 아키텍처 정의
embedding_dim = 256
encoder_units = 512
decoder_units = 512

# 인코더 정의
encoder_input = tf.keras.layers.Input(shape=(None,))
encoder_embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)(encoder_input)
encoder_lstm = tf.keras.layers.LSTM(encoder_units, return_state=True)
encoder_output, state_h, state_c = encoder_lstm(encoder_embedding)

# 디코더 정의
decoder_input = tf.keras.layers.Input(shape=(None,))
decoder_embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)(decoder_input)
decoder_lstm = tf.keras.layers.LSTM(decoder_units, return_sequences=True, return_state=True)
decoder_output, _, _ = decoder_lstm(decoder_embedding, initial_state=[state_h, state_c])
decoder_dense = tf.keras.layers.Dense(vocab_size, activation='softmax')
output = decoder_dense(decoder_output)

# 모델 생성
model = tf.keras.models.Model([encoder_input, decoder_input], output)

# 모델 컴파일
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 모델 훈련
model.fit([input_sequences, target_sequences[:, :-1]], target_sequences[:, 1:], epochs=50)

# 새로운 문장에 대한 답변 생성
def generate_response(input_text):
    try:
        # Attempt to cast the input_text to a float
        input_number = float(input_text)
        
        # Perform operations with the float value
        response_text = f"The float value is {input_number}"
    except ValueError:
        # Handle the case where the input_text cannot be cast to a float
        response_text = "Invalid input. Please enter a valid number."

    return response_text

# Example usage
user_input = "3.14"
response = generate_response(user_input)
print(response)

# 대화 테스트
user_input = "안녕!"
response = generate_response(user_input)
print(f"사용자: {user_input}")
print(f"챗봇: {response}")
