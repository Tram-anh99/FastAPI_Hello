<script setup>
import { ref, onMounted } from 'vue'

const danhSachMon = ref([])
const tenMonMoi = ref('')
const giaMoi = ref(0)
const API_URL = "http://127.0.0.1:8001" // Nhớ kiểm tra lại Port 8000 hay 8001

// ... (Hàm layDanhSach và themMon giữ nguyên như cũ) ...
const layDanhSach = async () => {
  const response = await fetch(`${API_URL}/danh-sach-mon`)
  danhSachMon.value = await response.json()
}

const themMon = async () => {
  if (!tenMonMoi.value) return
  await fetch(`${API_URL}/them-mon`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ ten_mon: tenMonMoi.value, gia: giaMoi.value })
  })
  tenMonMoi.value = ''; giaMoi.value = 0;
  layDanhSach()
}

// --- HÀM MỚI: XÓA MÓN ---
const xoaMon = async (id) => {
  if (confirm("Bạn có chắc muốn xóa món này không?")) {
    await fetch(`${API_URL}/xoa-mon/${id}`, {
      method: 'DELETE'
    })
    layDanhSach() // Tải lại danh sách sau khi xóa
  }
}

onMounted(() => {
  layDanhSach()
})
</script>

<template>
  <div class="container">
    <h1>🍽 Menu Quán Ăn FastAPI</h1>

    <div class="input-group">
      <input v-model="tenMonMoi" placeholder="Tên món ăn..." />
      <input v-model="giaMoi" type="number" placeholder="Giá tiền..." />
      <button @click="themMon">Thêm Món</button>
    </div>

    <ul>
      <li v-for="mon in danhSachMon" :key="mon.id">
        <div>
          <strong>{{ mon.ten_mon }}</strong>
          <span> - {{ mon.gia }} VND</span>
        </div>
        <button class="btn-xoa" @click="xoaMon(mon.id)">Xóa</button>
      </li>
    </ul>
  </div>
</template>

<style scoped>
/* ... (Style cũ giữ nguyên) ... */
.container {
  max-width: 600px;
  margin: 0 auto;
  font-family: sans-serif;
  padding: 20px;
}

h1 {
  color: #42b983;
  text-align: center;
}

.input-group {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

input {
  padding: 8px;
  flex: 1;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 8px 16px;
  background: #42b983;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 4px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  background: #f9f9f9;
  border-bottom: 1px solid #eee;
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

/* Style cho nút xóa */
.btn-xoa {
  background: #ff4d4d;
  margin-left: 10px;
}

.btn-xoa:hover {
  background: #cc0000;
}
</style>