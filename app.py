import streamlit as st
from datetime import datetime

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="Hóa đơn phòng trọ",
    page_icon="🏠",
    layout="centered"
)

# ==============================
# TIÊU ĐỀ
# ==============================
st.title("🏠 ỨNG DỤNG TÍNH HÓA ĐƠN PHÒNG TRỌ")
st.caption("Tiền phòng + Tiền điện + Tiền nước + Tiền WiFi")

st.divider()

# ==============================
# THÔNG TIN PHÒNG
# ==============================
st.subheader("📋 Thông tin phòng")

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

# ==============================
# TIỀN ĐIỆN
# ==============================
st.subheader("⚡ Tiền điện")

col1, col2 = st.columns(2)

with col1:
    dien_cu = st.number_input(
        "Chỉ số điện cũ (kWh)",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

with col2:
    dien_moi = st.number_input(
        "Chỉ số điện mới (kWh)",
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

# Tính số điện sử dụng
so_kwh = dien_moi - dien_cu

# Kiểm tra chỉ số
if dien_moi < dien_cu:
    st.error("⚠️ Chỉ số điện mới không được nhỏ hơn chỉ số điện cũ!")
    so_kwh = 0

tien_dien = so_kwh * don_gia_dien

st.info(
    f"⚡ Điện sử dụng: **{so_kwh:,.0f} kWh**  \n"
    f"💰 Tiền điện: **{tien_dien:,.0f} VNĐ**"
)

# ==============================
# TIỀN NƯỚC
# ==============================
st.subheader("💧 Tiền nước")

col3, col4 = st.columns(2)

with col3:
    nuoc_cu = st.number_input(
        "Chỉ số nước cũ (m³)",
        min_value=0.0,
        value=0.0,
        step=1.0
    )

with col4:
    nuoc_moi = st.number_input(
        "Chỉ số nước mới (m³)",
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

# Tính số nước sử dụng
so_m3 = nuoc_moi - nuoc_cu

# Kiểm tra chỉ số
if nuoc_moi < nuoc_cu:
    st.error("⚠️ Chỉ số nước mới không được nhỏ hơn chỉ số nước cũ!")
    so_m3 = 0

tien_nuoc = so_m3 * don_gia_nuoc

st.info(
    f"💧 Nước sử dụng: **{so_m3:,.0f} m³**  \n"
    f"💰 Tiền nước: **{tien_nuoc:,.0f} VNĐ**"
)

# ==============================
# TIỀN WIFI
# ==============================
st.subheader("📶 Tiền WiFi")

tien_wifi = st.number_input(
    "Tiền WiFi (VNĐ)",
    min_value=0,
    value=100000,
    step=10000,
    format="%d"
)

# ==============================
# NÚT TÍNH HÓA ĐƠN
# ==============================
st.divider()

if st.button(
    "🧮 TÍNH HÓA ĐƠN",
    use_container_width=True
):

    if not so_phong.strip():
        st.warning("⚠️ Vui lòng nhập số phòng!")

    elif dien_moi < dien_cu:
        st.warning("⚠️ Vui lòng kiểm tra lại chỉ số điện!")

    elif nuoc_moi < nuoc_cu:
        st.warning("⚠️ Vui lòng kiểm tra lại chỉ số nước!")

    else:

        # Tổng tiền
        tong_tien = (
            tien_phong
            + tien_dien
            + tien_nuoc
            + tien_wifi
        )

        # Lưu dữ liệu
        st.session_state["da_tinh"] = True
        st.session_state["so_phong"] = so_phong
        st.session_state["tien_phong"] = tien_phong

        st.session_state["dien_cu"] = dien_cu
        st.session_state["dien_moi"] = dien_moi
        st.session_state["so_kwh"] = so_kwh
        st.session_state["don_gia_dien"] = don_gia_dien
        st.session_state["tien_dien"] = tien_dien

        st.session_state["nuoc_cu"] = nuoc_cu
        st.session_state["nuoc_moi"] = nuoc_moi
        st.session_state["so_m3"] = so_m3
        st.session_state["don_gia_nuoc"] = don_gia_nuoc
        st.session_state["tien_nuoc"] = tien_nuoc

        st.session_state["tien_wifi"] = tien_wifi
        st.session_state["tong_tien"] = tong_tien


# ==============================
# HIỂN THỊ HÓA ĐƠN
# ==============================
if st.session_state.get("da_tinh", False):

    st.divider()

    st.subheader("🧾 HÓA ĐƠN TIỀN PHÒNG")

    st.markdown(
        f"### 🏠 Phòng: `{st.session_state['so_phong']}`"
    )

    # --------------------------
    # TIỀN PHÒNG
    # --------------------------
    st.write("🏠 **Tiền phòng**")
    st.write(
        f"Thành tiền: **{st.session_state['tien_phong']:,.0f} VNĐ**"
    )

    # --------------------------
    # TIỀN ĐIỆN
    # --------------------------
    st.write("⚡ **Tiền điện**")

    st.write(
        f"""
- Chỉ số cũ: **{st.session_state['dien_cu']:,.0f} kWh**
- Chỉ số mới: **{st.session_state['dien_moi']:,.0f} kWh**
- Số điện sử dụng: **{st.session_state['so_kwh']:,.0f} kWh**
- Đơn giá: **{st.session_state['don_gia_dien']:,.0f} VNĐ/kWh**
- Tiền điện: **{st.session_state['tien_dien']:,.0f} VNĐ**
"""
    )

    # --------------------------
    # TIỀN NƯỚC
    # --------------------------
    st.write("💧 **Tiền nước**")

    st.write(
        f"""
- Chỉ số cũ: **{st.session_state['nuoc_cu']:,.0f} m³**
- Chỉ số mới: **{st.session_state['nuoc_moi']:,.0f} m³**
- Số nước sử dụng: **{st.session_state['so_m3']:,.0f} m³**
- Đơn giá: **{st.session_state['don_gia_nuoc']:,.0f} VNĐ/m³**
- Tiền nước: **{st.session_state['tien_nuoc']:,.0f} VNĐ**
"""
    )

    # --------------------------
    # WIFI
    # --------------------------
    st.write("📶 **Tiền WiFi**")
    st.write(
        f"Thành tiền: **{st.session_state['tien_wifi']:,.0f} VNĐ**"
    )

    st.divider()

    # ==========================
    # TỔNG TIỀN
    # ==========================
    st.success(
        f"💵 TỔNG TIỀN CẦN THANH TOÁN: "
        f"{st.session_state['tong_tien']:,.0f} VNĐ"
    )

    # ==========================
    # THANH TOÁN
    # ==========================
    if st.button(
        "💳 THANH TOÁN & XUẤT HÓA ĐƠN",
        use_container_width=True
    ):

        thoi_gian = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

        # Nội dung file hóa đơn
        hoa_don = f"""
========================================
          HÓA ĐƠN TIỀN PHÒNG TRỌ
========================================

Số phòng: {st.session_state['so_phong']}
Ngày thanh toán: {thoi_gian}

----------------------------------------
TIỀN PHÒNG
----------------------------------------
{st.session_state['tien_phong']:,.0f} VNĐ

----------------------------------------
TIỀN ĐIỆN
----------------------------------------
Chỉ số cũ: {st.session_state['dien_cu']:,.0f} kWh
Chỉ số mới: {st.session_state['dien_moi']:,.0f} kWh
Số điện sử dụng: {st.session_state['so_kwh']:,.0f} kWh
Đơn giá: {st.session_state['don_gia_dien']:,.0f} VNĐ/kWh
Tiền điện: {st.session_state['tien_dien']:,.0f} VNĐ

----------------------------------------
TIỀN NƯỚC
----------------------------------------
Chỉ số cũ: {st.session_state['nuoc_cu']:,.0f} m³
Chỉ số mới: {st.session_state['nuoc_moi']:,.0f} m³
Số nước sử dụng: {st.session_state['so_m3']:,.0f} m³
Đơn giá: {st.session_state['don_gia_nuoc']:,.0f} VNĐ/m³
Tiền nước: {st.session_state['tien_nuoc']:,.0f} VNĐ

----------------------------------------
TIỀN WIFI
----------------------------------------
{st.session_state['tien_wifi']:,.0f} VNĐ

========================================
TỔNG CỘNG:
{st.session_state['tong_tien']:,.0f} VNĐ
========================================

TRẠNG THÁI: ĐÃ THANH TOÁN

Cảm ơn quý khách!
========================================
"""

        st.success("✅ THANH TOÁN THÀNH CÔNG!")

        st.write(
            f"Phòng **{st.session_state['so_phong']}** "
            f"đã thanh toán "
            f"**{st.session_state['tong_tien']:,.0f} VNĐ**."
        )

        # Nút tải hóa đơn
        st.download_button(
            label="📥 TẢI HÓA ĐƠN",
            data=hoa_don,
            file_name=(
                f"hoa_don_phong_"
                f"{st.session_state['so_phong']}.txt"
            ),
            mime="text/plain",
            use_container_width=True
        )
