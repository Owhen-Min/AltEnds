<template>
  <div v-if="isVisible" class="modal-overlay">
    <div class="modal">
      <h3>프롬프트와 결말 선택</h3>
      <div class="prompt-list">
        <div v-for="(ending, index) in altendings" :key="index" class="prompt-item">
          <input
            type="radio"
            :id="'ending-' + index"
            :value="ending"
            v-model="selectedEnding"
          />
          <label :for="'ending-' + index">
            <strong>프롬프트:</strong> {{ ending.prompt }} <br />
            <strong>대체 결말:</strong> {{ ending.content }}
          </label>
        </div>
      </div>
      <button @click="confirmSelection" :disabled="!selectedEnding">선택 완료</button>
      <button @click="closeModal">닫기</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Modal의 가시성 상태를 관리하는 prop
const props = defineProps({
  altendings: Array, // 전달된 대체 결말 목록
  isVisible: Boolean, // 모달의 표시 여부
});

// 모달 닫기
const closeModal = () => {
  props.isVisible = false;
};

// 선택된 결말 저장
const selectedEnding = ref(null);

// 선택한 프롬프트와 결말을 부모에게 전달
const confirmSelection = () => {
  if (selectedEnding.value) {
    props.$emit('select', selectedEnding.value);
    closeModal();
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed; /* 화면에 고정 */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* 배경을 반투명하게 */
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* 다른 콘텐츠보다 위에 표시 */
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  max-height: 80vh; /* 모달의 최대 높이를 80%로 설정 */
  overflow-y: auto; /* 내용이 많으면 스크롤 가능 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  z-index: 2000; /* 다른 콘텐츠보다 위에 표시 */
}

.prompt-list {
  margin-bottom: 20px;
  max-height: 300px; /* 너무 길어지지 않게 제한 */
  overflow-y: auto; /* 스크롤 추가 */
}

.prompt-item {
  margin-bottom: 10px;
}

button {
  padding: 10px;
  margin-top: 10px;
  cursor: pointer;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
}

button:disabled {
  background-color: #ddd;
}

button + button {
  margin-left: 10px;
}

h3 {
  margin-bottom: 20px;
  font-size: 18px;
}

label {
  font-size: 14px;
}
</style>
