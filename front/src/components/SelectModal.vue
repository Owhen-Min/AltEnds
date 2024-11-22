<template>
  <div class="modal" v-if="isOpen">
    <div class="modal-content">
      <h3>{{ title }}</h3>
      <p>{{ message }}</p>

      <!-- 프롬프트 선택 리스트 -->
      <div v-if="options && options.length > 0">
        <p>선택 가능한 프롬프트:</p>
        <ul class="options-list">
          <li
            v-for="(option, index) in options"
            :key="index"
            :class="['option-item', selectedIndex === index ? 'selected' : '']"
            @click="selectOption(index)"
          >
            {{ option.prompt }}
          </li>
        </ul>
      </div>

      <!-- 선택된 결말 표시 -->
      <div v-if="selectedIndex !== null">
        <h5>선택한 프롬프트와 결말</h5>
        <p><strong>프롬프트:</strong> {{ options[selectedIndex].prompt }}</p>
        <p><strong>대체 결말:</strong> {{ options[selectedIndex].content }}</p>
      </div>

      <div class="modal-actions">
        <button @click="onConfirm" class="btn btn-primary" :disabled="selectedIndex === null">확인</button>
        <button @click="onCancel" class="btn btn-secondary">취소</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

defineProps({
  isOpen: Boolean,
  title: String,
  message: String,
  options: Array, // 프롬프트와 결말 리스트
});

const emit = defineEmits(['confirm', 'cancel']);

const selectedIndex = ref(null);

const selectOption = (index) => {
  selectedIndex.value = index;
};

const onConfirm = () => {
  if (selectedIndex.value !== null) {
    emit('confirm', selectedIndex.value); // 선택한 인덱스를 부모로 전달
  }
};

const onCancel = () => {
  emit('cancel');
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  width: 400px;
  text-align: center;
}

.options-list {
  list-style: none;
  padding: 0;
  margin: 10px 0;
  max-height: 150px;
  overflow-y: auto;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.option-item {
  padding: 10px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.option-item:hover {
  background-color: #f1f1f1;
}

.option-item.selected {
  background-color: #17a2b8;
  color: white;
}

.modal-actions {
  margin-top: 20px;
  display: flex;
  justify-content: space-around;
}
</style>
