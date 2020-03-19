clear; clc;
%% 数据处理
data_temp = imread('./2.png');
data_2 = data_temp(135:719,219:1059,1);
data_2 = [data_2; zeros(256,841)];
path = './Screenshot_2020-03-20-01-54-08.png';
data_temp = imread(path);
test_2 = data_temp(135:719,219:1059,1);
test_2 = [test_2; zeros(256,841)];
%% 剪切剩扇形
for i = 1:841 %行
    for j = 1:841 %列
        dis = sqrt(power(i-421,2)+power(j-421,2));
        if dis < 142.8 || dis > 420.5
            test_2(i,j) = 0;
            data_2(i,j) = 0;
        end
    end
end
% test = imrotate(test_2,16,'nearest','crop');
% imshow(test_2);
% hold on;
% x = 1:420;
% y = 420 - (420-x)*abs(tan(165/180*pi));
% plot(x,y,'.');

% for i = 1:420 %行
% 	for j = 1:420 %列
%         tann = (421-j)/(421-i);
%         if tann <= tan_bigger && tann >= tan_lower
%             test(j,i) = 255;
%         end
% 	end
% end
% imshow(test);
%% 开始旋转
N = 10;
left_angle = 170;
angle_space = 160 / N;
show_range = [left_angle-angle_space+4.5, left_angle-4.5];
tan_bigger = abs(tan(show_range(1)/180*pi));
tan_lower = abs(tan(show_range(2)/180*pi));

% % 演示剪切剩最左扇形
% data_rotate = imrotate(data_2,16*0,'nearest','crop');
% data_rotate(421:end,:) = 0;
% data_rotate(:,421:end) = 0;
% for i = 1:420 %行
% 	for j = 1:420 %列
%         tann = (421-j)/(421-i);
%         if tann > tan_bigger || tann < tan_lower
%             data_rotate(j,i) = 0;
%         end
% 	end
% end
% imshow(data_rotate);

% % x = 1:421;
% % y1 = 421 - (421-x)*abs(tan(166.5/180*pi));
% % y2 = 421 - (421-x)*abs(tan(157.5/180*pi));
% % plot(x,y1,'.');
% % plot(x,y2,'.');

data_slice = zeros(420,420,3);
data_slice = uint8(data_slice);
for n = 1:N
    data_rotate = imrotate(data_2,angle_space*(n-1),'nearest','crop');
    for i = 1:420 %行
        for j = 1:420 %列
            tann = (421-j)/(421-i);
            if tann > tan_bigger || tann < tan_lower
                data_rotate(j,i) = 0;
            end
        end
    end
    data_slice(:,:,n) = data_rotate(1:420,1:420);
end
% imshow(data_slice(:,:,5));

test_slice = zeros(420,420,3);
test_slice = uint8(test_slice);
for n = 1:N
    test_rotate = imrotate(test_2,angle_space*(n-1),'nearest','crop');
    for i = 1:420 %行
        for j = 1:420 %列
            tann = (421-j)/(421-i);
            if tann > tan_bigger || tann < tan_lower
                test_rotate(j,i) = 0;
            end
        end
    end
    test_slice(:,:,n) = test_rotate(1:420,1:420);
end
% imshow(test_slice(:,:,5));

total_cha = [];
for i = 1:N
    minus = data_slice - test_slice(:,:,i);
    cha = sum(sum(minus,2),1);
    cha = reshape(cha, 1, N);
    total_cha = [total_cha;cha]
end

[c,t] = hungarian(total_cha');%每个位置放的第几块正确拼图

%% 按顺序恢复

move = zeros(1,N);
for i = 1:N
    [sorted, idx] = sort(c);
    if c(i)~=i
        move(i) = idx(i);
        t = c(i);
        c(i) = c(idx(i));
        c(idx(i)) = t;
    else
       move(i) = 0;;% 0不用移动
    end
end
disp(move);