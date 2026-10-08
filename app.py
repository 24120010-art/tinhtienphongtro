import streamlit as st
from datetime import datetime

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Tính hóa đơn phòng trọ",
    page_icon="🏠",
    layout="centered"
)

# =========================
# TIÊU ĐỀ
# =========================
st.title("🏠 ỨNG DỤNG TÍNH HÓA ĐƠN PHÒNG TRỌ")
st.write("Tính tiền phòng, tiền điện, tiền nước và tiền WiFi")

st.divider()

# =========================
# NHẬP THÔNG TIN
# =========================
st.subheader("📋 Thông tin hóa đơn")

so_phong = st.text_input(
    "🏠 Số phòng",
    placeholder="Ví dụ: P101"
)

tien_phong = st.number_input(
    "💰 Tiền phòng (VNĐ)",
    min_value=0,
    value=3000000,
    step=100000,
    format="%d"
)

st.markdown("### ⚡ Tiền điện")

so_dien = st.number_input(
    "Số điện sử dụng (kWh)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

don_gia_dien = st.number_input(
    "Đơn giá điện (VNĐ/kWh)",
    min_value=0,
    value=3500,
    step=100,
    format="%d"
)

st.markdown("### 💧 Tiền nước")

so_nuoc = st.number_input(
    "Số nước sử dụng (m³)",
    min_value=0.0,
    value=0.0,
    step=1.0
)

don_gia_nuoc = st.number_input(
    "Đơn giá nước (VNĐ/m³)",
    min_value=0,
    value=15000,
    step=1000,
    format="%d"
)

st.markdown("### 📶 Tiền WiFi")

tien_wifi = st.number_input(
    "Tiền WiFi (VNĐ)",
    min_value=0,
    value=100000,
    step=10000,
    format="%d"
)

# =========================
# NÚT TÍNH HÓA ĐƠN
# =========================
if st.button("🧮 TÍNH HÓA ĐƠN", use_container_width=True):

    if not so_phong.strip():
        st.warning("⚠️ Vui lòng nhập số phòng!")
    else:
        # Tính tiền điện
        tien_dien = so_dien * don_gia_dien

        # Tính tiền nước
        tien_nuoc = so_nuoc * don_gia_nuoc

        # Tổng tiền
        tong_tien = (
            tien_phong
            + tien_dien
            + tien_nuoc
            + tien_wifi
        )

        # Lưu thông tin vào session
        st.session_state["da_tinh"] = True
        st.session_state["so_phong"] = so_phong
        st.session_state["tien_phong"] = tien_phong
        st.session_state["so_dien"] = so_dien
        st.session_state["don_gia_dien"] = don_gia_dien
        st.session_state["tien_dien"] = tien_dien
        st.session_state["so_nuoc"] = so_nuoc
        st.session_state["don_gia_nuoc"] = don_gia_nuoc
        st.session_state["tien_nuoc"] = tien_nuoc
        st.session_state["tien_wifi"] = tien_wifi
        st.session_state["tong_tien"] = tong_tien

# =========================
# HIỂN THỊ KẾT QUẢ
# =========================
if st.session_state.get("da_tinh", False):

    st.divider()

    st.subheader("🧾 CHI TIẾT HÓA ĐƠN")

    st.info(
        f"🏠 **Số phòng:** {st.session_state['so_phong']}"
    )

    # Bảng hóa đơn
    du_lieu = {
        "Khoản thu": [
            "Tiền phòng",
            "Tiền điện",
            "Tiền nước",
            "Tiền WiFi"
        ],
        "Chi tiết": [
            "Theo tháng",
            f"{st.session_state['so_dien']:.0f} kWh × "
            f"{st.session_state['don_gia_dien']:,.0f} VNĐ",
            f"{st.session_state['so_nuoc']:.0f} m³ × "
            f"{st.session_state['don_gia_nuoc']:,.0f} VNĐ",
            "Theo tháng"
        ],
        "Thành tiền": [
            f"{st.session_state['tien_phong']:,.0f} VNĐ",
            f"{st.session_state['tien_dien']:,.0f} VNĐ",
            f"{st.session_state['tien_nuoc']:,.0f} VNĐ",
            f"{st.session_state['tien_wifi']:,.0f} VNĐ"
        ]
    }

    st.table(du_lieu)

    # Tổng tiền
    st.success(
        f"💵 TỔNG TIỀN CẦN THANH TOÁN: "
        f"{st.session_state['tong_tien']:,.0f} VNĐ"
    )

    st.divider()

    # =========================
    # THANH TOÁN
    # =========================
    if st.button(
        "💳 THANH TOÁN & XUẤT HÓA ĐƠN",
        use_container_width=True
    ):

        thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        # Nội dung hóa đơn
        hoa_don = f"""
========================================
          HÓA ĐƠN TIỀN PHÒNG TRỌ
========================================

Số phòng: {st.session_state['so_phong']}
Thời gian: {thoi_gian}

----------------------------------------
CHI TIẾT THANH TOÁN
----------------------------------------

Tiền phòng:
{st.session_state['tien_phong']:,.0f} VNĐ

Tiền điện:
{st.session_state['so_dien']:.0f} kWh
Đơn giá: {st.session_state['don_gia_dien']:,.0f} VNĐ/kWh
Thành tiền: {st.session_state['tien_dien']:,.0f} VNĐ

Tiền nước:
{st.session_state['so_nuoc']:.0f} m³
Đơn giá: {st.session_state['don_gia_nuoc']:,.0f} VNĐ/m³
Thành tiền: {st.session_state['tien_nuoc']:,.0f} VNĐ

Tiền WiFi:
{st.session_state['tien_wifi']:,.0f} VNĐ

----------------------------------------
TỔNG CỘNG:
{st.session_state['tong_tien']:,.0f} VNĐ
----------------------------------------

TRẠNG THÁI: ĐÃ THANH TOÁN

Cảm ơn quý khách!
========================================
"""

        st.success("✅ Thanh toán thành công!")

        st.write(
            f"**Phòng {st.session_state['so_phong']} "
            f"đã thanh toán {st.session_state['tong_tien']:,.0f} VNĐ.**"
        )

        # Cho phép tải hóa đơn
        st.download_button(
            label="📥 TẢI HÓA ĐƠN",
            data=hoa_don,
            file_name=f"hoa_don_phong_{st.session_state['so_phong']}.txt",
            mime="text/plain",
            use_container_width=True
        )
