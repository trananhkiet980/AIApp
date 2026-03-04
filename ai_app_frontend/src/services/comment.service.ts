



import { Injectable } from '@angular/core';
import { Comment } from '../models/comment.model';
import { Observable, of } from 'rxjs';

@Injectable({
	providedIn: 'root'
})
export class CommentService {
	// Hàm lấy danh sách bình luận (Mô phỏng XMLHttpRequest) 
	getComments(): Observable<Comment[]> {
		const mockComments: Comment[] = [
			{ id: 1, author: 'Kiet', content: 'Dự án AI này rất thú vị!' },
			{ id: 2, author: 'Admin', content: 'Cấu trúc Angular chuẩn Rakumo.' }
		];
		return of(mockComments);
	}
}