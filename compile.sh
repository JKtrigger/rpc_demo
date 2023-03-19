@echo off

echo [1/3] Copying files...
mkdir -p ./chat/proto
cp ./protos/__init__.py ./chat/proto/__init__.py
echo [2/3] Generating proto...
python -m grpc_tools.protoc --proto_path=./protos/ --python_out=./chat/proto --grpc_python_out=./chat/proto ./protos/chat.proto
python setup.py sdist bdist_wheel
echo "[3/3] Delete artists"
cp ./dist/chat-0.0.1-py3-none-any.whl ./chat-0.0.1-py3-none-any.whl
rm -rf ./chat.egg-info
rm -rf  ./dist
rm -rf  ./build
rm -rf  ./chat
echo "[1/1] install packages"
pip install --force-reinstall chat-0.0.1-py3-none-any.whl
rm chat-0.0.1-py3-none-any.whl
ls /home/runner/.local/lib/python3.10/site-packages/chat/
ls /home/runner/.local/lib/python3.10/site-packages/chat/proto

python ./main.py

