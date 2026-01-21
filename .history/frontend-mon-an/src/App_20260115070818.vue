<script setup>
import { ref, onMounted } from 'vue'

// 1. Khai báo biến để chứa dữ liệu
const danhSachMon = ref([])
const tenMonMoi = ref('')
const giaMoi = ref(0)

// LƯU Ý QUAN TRỌNG: Nếu FastAPI của bạn chạy port 8001 thì sửa số 8000 thành 8001 ở dưới nhé!
const API_URL = "http://127.0.0.1:8001"

// 2. Hàm lấy danh sách món từ FastAPI
const layDanhSach = async () => {
  try {
    const response = await fetch(`${API_URL}/danh-sach-mon`)
    danhSachMon.value = await response.json()
  } catch (error) {
    console.error("Lỗi khi lấy dữ liệu:", error)
    alert("Không kết nối được với FastAPI! Kiểm tra lại Port xem.")
  }
}

// 3. Hàm thêm món mới
const themMon = async () => {
  if (!tenMonMoi.value) return alert("Chưa nhập tên món!")

  await fetch(`${API_URL}/them-mon`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      ten_mon: tenMonMoi.value,
      gia: giaMoi.value
    })
  })

  // Thêm xong thì xóa ô nhập và tải lại danh sách
  tenMonMoi.value = ''
  giaMoi.value = 0
  layDanhSach()
}

// 4. Khi trang web vừa hiện lên thì gọi hàm lấy danh sách ngay
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
        <strong>{{ mon.ten_mon }}</strong>
        <span> - {{ mon.gia }} VND</span>
      </li>
    </ul>

    <p v-if="danhSachMon.length === 0">Chưa có món nào, hãy thêm thử xem!</p>
  </div>
</template>

<style scoped>
/* Trang trí một chút cho đẹp */
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

button:hover {
  background: #3aa876;
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
}
</style>