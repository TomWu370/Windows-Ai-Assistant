mkdir build
cd build
cmake ..
cmake --build . --config Release
for %%I in (Release\*.pyd) do move "%%I" ..
