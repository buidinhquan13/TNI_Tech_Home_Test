   
# import streamlit as st
# from detector import detect_person
# from database import init_db, save_result, get_results, delete_old_data_and_images
# from PIL import Image
# from pathlib import Path
# import os

# init_db()

# # Tự động xóa dữ liệu và ảnh cũ hơn 30 ngày
# delete_old_data_and_images(days=30)

# st.title("Person Detection System")

# tab1, tab2 = st.tabs(["📤 Upload & Detect", "📜 History"])

# with tab1:
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp", "gif"])
#     if uploaded_file:
#         # image_path = save_uploaded_file(uploaded_file)
#         person_count, vis_path = detect_person(uploaded_file, "results")
#         save_result(person_count, vis_path)

#         # st.image(vis_path, caption=f"Detected {person_count} person(s)", use_container_width=True)
#         st.image(vis_path, use_container_width=True)

#         # Caption to đậm
#         st.markdown(
#             f"<h4 style='text-align: center; color: green;'>Detected {person_count} person(s)</h4>",
#             unsafe_allow_html=True
#         )


# with tab2:
#     # Khởi tạo state mặc định nếu chưa có
#     if "page" not in st.session_state:
#         st.session_state.page = 1

#     # Thanh tìm kiếm
#     search = st.text_input("", placeholder="Search image path")

#     # Cấu hình phân trang
#     page = st.session_state.page
#     limit = 10  # 5 hàng x 2 cột = 10 ảnh
#     offset = (page - 1) * limit

#     results, total = get_results(search=search, limit=limit, offset=offset)
#     total_pages = (total + limit - 1) // limit

#     st.markdown(f"<b>Total Records: </b> {total} | Page {page} of {total_pages}", unsafe_allow_html=True)

#     # Hiển thị kết quả dạng lưới
#     cols = 2
#     for i in range(0, len(results), cols):
#         cols_layout = st.columns(cols)
#         for j in range(cols):
#             if i + j < len(results):
#                 r = results[i + j]
#                 with cols_layout[j]:
#                     st.markdown(
#                         f"<b>Time:</b> {r.timestamp}<br>"
#                         f"<b>People:</b> {r.person_count}<br>"
#                         f"<b>Image Name:</b> {os.path.basename(r.image_path)}<br>"
#                         f"<b>Image Path:</b> {r.image_path}",
#                         unsafe_allow_html=True
#                     )

#                     image_path = Path(r.image_path).as_posix()
#                     if os.path.exists(image_path):
#                         st.image(image_path, width=400)
#                     else:
#                         st.warning("⚠️ Image not found")

#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button("Previous"):
#             if st.session_state.page > 1:
#                 st.session_state.page -= 1

#     with col2:
#         if st.button("Next"):
#             if st.session_state.page < total_pages:
#                 st.session_state.page += 1

#     # Lưu lại trạng thái page mới sau khi nhấn nút
#     if "page" in st.session_state:
#         st.session_state.page = page

# import streamlit as st
# from detector import detect_person
# from database import init_db, save_result, get_results, delete_old_data_and_images
# from PIL import Image
# from pathlib import Path
# import os


# init_db()
# delete_old_data_and_images(days=30)

# st.title("Person Detection System")

# tab1, tab2 = st.tabs(["📤 Upload & Detect", "📜 History"])

# # with tab1:
# #     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp", "gif"])
# #     if uploaded_file:
# #         person_count, vis_path = detect_person(uploaded_file, "results")
# #         save_result(person_count, vis_path)

# #         st.image(vis_path, use_container_width=True)
# #         st.markdown(
# #             f"<h4 style='text-align: center; color: green;'>Detected {person_count} person(s)</h4>",
# #             unsafe_allow_html=True
# #         )

# with tab1:
#     uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp", "gif"])

#     if uploaded_file and "last_uploaded" not in st.session_state:
#         person_count, vis_path = detect_person(uploaded_file, "results")
#         save_result(person_count, vis_path)
#         st.session_state.last_uploaded = uploaded_file.name  # Lưu tên ảnh vào state

#         st.image(vis_path, use_container_width=True)
#         st.markdown(
#             f"<h4 style='text-align: center; color: green;'>Detected {person_count} person(s)</h4>",
#             unsafe_allow_html=True
#         )
#     elif uploaded_file and st.session_state.get("last_uploaded") == uploaded_file.name:
#         # Chỉ hiển thị lại ảnh đã xử lý, không xử lý lại
#         vis_path = f"results/{uploaded_file.name.split('.')[0]}_detected.png"
#         st.image(vis_path, use_container_width=True)

# with tab2:
    
#     search = st.text_input("", placeholder="Search image path")

#     # Khởi tạo state mặc định
#     if "page" not in st.session_state:
#         st.session_state.page = 1

#     page = st.session_state.page
#     limit = 10
#     offset = (page - 1) * limit

#     results, total = get_results(search=search, limit=limit, offset=offset)
#     total_pages = max((total + limit - 1) // limit, 1)

#     # Nút điều hướng
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button("⬅️ Previous") and st.session_state.page > 1:
#             st.session_state.page -= 1
#             #st.rerun()  # Dòng này bắt buộc để cập nhật giao diện

#     with col2:
#         if st.button("Next ➡️") and st.session_state.page < total_pages:
#             st.session_state.page += 1
#             #st.rerun()  # Dòng này bắt buộc để cập nhật giao diện

#     page = st.session_state.page  # Cập nhật lại biến page nếu cần
    

#     st.markdown(f"<b>Total Records: </b> {total} | Page {page} of {total_pages}", unsafe_allow_html=True)

#     cols = 2
#     for i in range(0, len(results), cols):
#         cols_layout = st.columns(cols)
#         for j in range(cols):
#             if i + j < len(results):
#                 r = results[i + j]
#                 with cols_layout[j]:
#                     st.markdown(
#                         f"<b>Time:</b> {r.timestamp}<br>"
#                         f"<b>People:</b> {r.person_count}<br>"
#                         f"<b>Image Name:</b> {os.path.basename(r.image_path)}<br>"
#                         f"<b>Image Path:</b> {r.image_path}",
#                         unsafe_allow_html=True
#                     )
#                     image_path = Path(r.image_path).as_posix()
#                     if os.path.exists(image_path):
#                         st.image(image_path, width=400)
#                     else:
#                         st.warning("⚠️ Image not found")



import streamlit as st
from detector import detect_person
from database import init_db, save_result, get_results, delete_old_data_and_images
from pathlib import Path
import os

# Khởi tạo DB & dọn ảnh cũ
init_db()
delete_old_data_and_images(days=30)

# Giao diện
st.title("Person Detection System")

# Tabs logic
tab_names = ["📤 Upload & Detect", "📜 History"]
selected_tab = st.selectbox("Select tab", tab_names, label_visibility="collapsed")
tab1_active = selected_tab == tab_names[0]
tab2_active = selected_tab == tab_names[1]

# ============================== TAB 1 ==============================
if tab1_active:
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png", "bmp", "tiff", "webp", "gif"])

    if uploaded_file:
        if st.session_state.get("last_uploaded") != uploaded_file.name:
            # Chỉ xử lý ảnh mới
            person_count, vis_path = detect_person(uploaded_file, "results")
            save_result(person_count, vis_path)
            st.session_state.last_uploaded = uploaded_file.name
        else:
            vis_path = f"results/{uploaded_file.name.split('.')[0]}_detected.png"

        st.image(vis_path, use_container_width=True)
        st.markdown(
            f"<h4 style='text-align: center; color: green;'>Detected {person_count} person(s)</h4>",
            unsafe_allow_html=True
        )

# ============================== TAB 2 ==============================
if tab2_active:
    # Thanh tìm kiếm
    search = st.text_input("", placeholder="Search image path")
    
    if "page" not in st.session_state:
        st.session_state.page = 1

    page = st.session_state.page
    limit = 8
    offset = (page - 1) * limit

    results, total = get_results(search=search, limit=limit, offset=offset)
    total_pages = max((total + limit - 1) // limit, 1)

    # Nút điều hướng
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Previous") and st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()  # <- Bắt buộc rerun để cập nhật trang ngay

    with col2:
        if st.button("Next") and st.session_state.page < total_pages:
            st.session_state.page += 1
            st.rerun()  # <- Bắt buộc rerun để cập nhật trang ngay
        # Cập nhật lại page
    page = st.session_state.page

    # Hiển thị phân trang
    st.markdown(f"<b>Total Records: </b> {total} | Page {page} of {total_pages}", unsafe_allow_html=True)

    # Hiển thị dạng lưới
    cols = 2
    for i in range(0, len(results), cols):
        cols_layout = st.columns(cols)
        for j in range(cols):
            if i + j < len(results):
                r = results[i + j]
                with cols_layout[j]:
                    st.markdown(
                        f"<b>Time:</b> {r.timestamp}<br>"
                        f"<b>People:</b> {r.person_count}<br>"
                        f"<b>Image Name:</b> {os.path.basename(r.image_path)}<br>"
                        f"<b>Image Path:</b> {r.image_path}",
                        unsafe_allow_html=True
                    )
                    image_path = Path(r.image_path).as_posix()
                    if os.path.exists(image_path):
                        st.image(image_path, width=400)
                    else:
                        st.warning("Image not found")


